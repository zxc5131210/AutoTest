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
            <title>Automation Test Report</title>
            <link href="./html_css/bootstrap.min.css" rel="stylesheet">
            <script src="./html_css/jquery.min.js"></script>
            <script src="./html_css/bootstrap.min.js"></script>
            <script>
            function filterTestCases(filterType) {
                switch (filterType) {
                    case "all":
                        // Display all categories and subcategories
                        $(".category, .subcategory").removeClass("hidden");
                        
                        // Display all test cases
                        $(".test-case").removeClass("hidden");
            
                        // Collapse passed test cases and expand failed test cases
                        $(".test-case.pass .test-case-content").hide();
                        $(".test-case.fail .test-case-content").show();
                        break;
            
                    case "pass":
                        // Display all categories and subcategories
                        $(".category, .subcategory").removeClass("hidden");
            
                        // Hide failed test cases and show passed test cases
                        $(".test-case.fail").addClass("hidden");
                        $(".test-case.pass").removeClass("hidden");
            
                        // Collapse all test cases
                        $(".test-case-content").hide();
            
                        // Hide subcategories without passed test cases
                        $(".subcategory").each(function() {
                            if ($(this).find(".test-case.pass:not(.hidden)").length == 0) {
                                $(this).addClass("hidden");
                            }
                        });
                        break;
            
                    case "fail":
                        // Display all categories and subcategories
                        $(".category, .subcategory").removeClass("hidden");
            
                        // Hide passed test cases and show failed test cases
                        $(".test-case.pass").addClass("hidden");
                        $(".test-case.fail").removeClass("hidden");
            
                        // Expand all failed test cases
                        $(".test-case.fail .test-case-content").show();
            
                        // Hide subcategories without failed test cases
                        $(".subcategory").each(function() {
                            if ($(this).find(".test-case.fail:not(.hidden)").length == 0) {
                                $(this).addClass("hidden");
                            }
                        });
                        break;
                }
            }
            
            // Ensure filterTestCases is called on document ready and button click
            $(document).ready(function() {
                // Bind the filterTestCases function to the filter buttons
                $(".filter-button").click(function() {
                    filterTestCases($(this).data("filter-type"));
                });
            
                // Default display
                filterTestCases("all");
            });
            </script>
        </head>
        <body>
        <div class="container">
        <h1 class='text-center'>Automation Test Report</h1>
        <div class="text-center">
            <button onclick="filterTestCases('all')" class="btn btn-default">All</button>
            <button onclick="filterTestCases('pass')" class="btn btn-success">Pass</button>
            <button onclick="filterTestCases('fail')" class="btn btn-danger">Fail</button>
        </div>
        <br>
        """

        for category, subcategories in self.categories.items():
            safe_category_id = category.replace(" ", "_").replace("-", "_")
            html += f"<div class='panel panel-primary category-panel'>"
            html += f"<div class='panel-heading' data-toggle='collapse' href='#collapse{safe_category_id}'>{category}</div>"
            html += f"<div id='collapse{safe_category_id}' class='panel-collapse collapse in'>"

            for subcat, testcases in subcategories.items():
                safe_subcat_id = subcat.replace(" ", "_").replace("-", "_")
                html += f"<div class='panel panel-info subcategory-panel'>"
                html += f"<div class='panel-heading' data-toggle='collapse' href='#collapse{safe_category_id}_{safe_subcat_id}'>{subcat}</div>"
                html += f"<div id='collapse{safe_category_id}_{safe_subcat_id}' class='panel-collapse collapse in'>"

                for idx, (testcase, detail, steps, status) in enumerate(testcases):
                    html += (
                        f"<div class='panel panel-default test-case {status.lower()}'>"
                    )
                    html += f"<div class='panel-heading' data-toggle='collapse' href='#collapse{safe_category_id}_{safe_subcat_id}_{idx}'>{testcase} - <span class='label label-{'danger' if status == 'Fail' else 'success'}'>{status}</span></div>"
                    html += (
                        f"<div id='collapse{safe_category_id}_{safe_subcat_id}_{idx}' class='panel-collapse "
                        f"collapse'>"
                    )
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
