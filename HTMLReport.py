class TestReport:
    def __init__(self):
        self.categories = {"vlauncher": {}, "STB": {}}

    def add_entry(self, category, subcategory, testcase, detail, steps, status):
        if subcategory not in self.categories[category]:
            self.categories[category][subcategory] = []
        self.categories[category][subcategory].append((testcase, detail, steps, status))

    def generate_html(self):
        html = """
        <html>
        <head>
            <title>Test Report</title>
            <link href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
            <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
            <script>
            function filterTestCases(filterType) {
                $(".category-panel, .subcategory-panel").show();
                $(".test-case").show();
                $(".test-case .panel-collapse").collapse('hide');

                if (filterType === "pass") {
                    $(".test-case.fail").hide();
                } else if (filterType === "fail") {
                    $(".test-case.pass").hide();
                    $(".test-case.fail .panel-collapse").collapse('show');
                }

                $(".subcategory-panel").each(function() {
                    if ($(this).find(".test-case:visible").length == 0) {
                        $(this).hide();
                    }
                });

                $(".category-panel").each(function() {
                    if ($(this).find(".subcategory-panel:visible").length == 0) {
                        $(this).hide();
                    }
                });
            }
            </script>
        </head>
        <body>
        <div class="container">
        <h1 class='text-center'>Test Cases Report</h1>
        <div class="text-center">
            <button onclick="filterTestCases('all')" class="btn btn-default">All</button>
            <button onclick="filterTestCases('pass')" class="btn btn-success">Pass</button>
            <button onclick="filterTestCases('fail')" class="btn btn-danger">Fail</button>
        </div>
        <br>
        """

        for category, subcategories in self.categories.items():
            html += f"<div class='panel panel-primary category-panel'>"
            html += f"<div class='panel-heading' data-toggle='collapse' href='#collapse{category}'>{category}</div>"
            html += f"<div id='collapse{category}' class='panel-collapse collapse in'>"

            for subcat, testcases in subcategories.items():
                html += f"<div class='panel panel-info subcategory-panel'>"
                html += f"<div class='panel-heading' data-toggle='collapse' href='#collapse{category}_{subcat}'>{subcat}</div>"
                html += f"<div id='collapse{category}_{subcat}' class='panel-collapse collapse in'>"

                for idx, (testcase, detail, steps, status) in enumerate(testcases):
                    html += (
                        f"<div class='panel panel-default test-case {status.lower()}'>"
                    )
                    html += f"<div class='panel-heading' data-toggle='collapse' href='#collapse{category}_{subcat}_{idx}'>{testcase} - <span class='label label-{'danger' if status == 'Fail' else 'success'}'>{status}</span></div>"
                    html += f"<div id='collapse{category}_{subcat}_{idx}' class='panel-collapse collapse'>"
                    html += f"<div class='panel-body'>{detail}</div>"
                    if steps:
                        html += "<ul>"
                        for step, step_status in steps.items():
                            step_label_class = (
                                "danger" if step_status == "Fail" else "success"
                            )
                            html += f"<li>{step} - <span class='label label-{step_label_class}'>{step_status}</span></li>"
                        html += "</ul>"
                    html += "</div></div>"

                html += "</div></div>"

            html += "</div></div>"

        html += """
        </div>
        </body>
        </html>
        """

        return html

    def save_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(self.generate_html())
