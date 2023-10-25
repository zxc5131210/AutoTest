# test_report.py


class TestReport:
    def __init__(self):
        self.categories = {"vlauncher": {}, "STB": {}}

    def add_entry(
        self, category, subcategory, testcase, detail, steps, status, comment=None
    ):
        if subcategory not in self.categories[category]:
            self.categories[category][subcategory] = []
        self.categories[category][subcategory].append(
            (testcase, detail, steps, status, comment)
        )

    def generate_html(self):
        html = """<html>
        <head>
            <title>Automation Test Report</title>
            <link href="./html_css/bootstrap.min.css" rel="stylesheet">
            <script src="./html_css/jquery.min.js"></script>
            <script src="./html_css/bootstrap.min.js"></script>
            <script src="./html_css/filter.js"></script>
            <style>
                #summary {
                    font-size: 20px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <h1 class='text-center'>Automation Test Report</h1>
                <div class="text-center">
                    <button onclick="filterTestCases('all')" class="btn btn-default">All</button>
                    <button onclick="filterTestCases('pass')" class="btn btn-success">Pass</button>
                    <button onclick="filterTestCases('fail')" class="btn btn-danger">Fail</button>
                    <div id="summary-card" class="card">
                        <div class="card-body">
                            <div id="summary" class="text-center alert summary-alert"></div>
                        </div>
                    </div>
                </div>
                <br>
                """

        # Iterate through categories and subcategories to build the report
        for category, subcategories in self.categories.items():
            safe_category_id = category.replace(" ", "_").replace("-", "_")
            html += f"<div class='panel panel-primary category-panel' id='category_{safe_category_id}'>"
            html += (
                f"<div class='panel-heading' data-toggle='collapse' "
                f"href='#collapse{safe_category_id}'>{category} "
                f"<span class='glyphicon glyphicon-chevron-down'></span></div>"
            )
            html += f"<div id='collapse{safe_category_id}' class='panel-collapse collapse in'>"

            for subclass, testcases in subcategories.items():
                safe_subcategories_id = subclass.replace(" ", "_").replace("-", "_")
                pass_count = sum(
                    1 for _, _, _, status, _ in testcases if status == "Pass"
                )
                total_count = len(testcases)

                html += (
                    f"<div class='panel panel-info subcategory-panel' "
                    f"id='category_{safe_category_id}_{safe_subcategories_id}'>"
                )
                html += (
                    f"<div class='panel-heading' data-toggle='collapse' "
                    f"href='#collapse{safe_category_id}_{safe_subcategories_id}'>"
                    f"{subclass} ({pass_count}/{total_count}) "
                    f"<span class='glyphicon glyphicon-chevron-down'></span></div>"
                )
                html += (
                    f"<div id='collapse{safe_category_id}_{safe_subcategories_id}' class='panel-collapse collapse "
                    f"in'>"
                )

                for idx, (testcase, detail, steps, status, comment) in enumerate(
                    testcases
                ):
                    panel_id = f"{safe_category_id}_{safe_subcategories_id}_{idx}"
                    html += (
                        f"<div class='panel panel-default test-case {status.lower()}'>"
                    )
                    html += (
                        f"<div class='panel-heading' data-toggle='collapse' "
                        f"href='#collapse{panel_id}'>"
                        f"{testcase} - "
                        f"<a href='#' onclick='openPopup(\"{status}\", \"{panel_id}\")'>"
                        f"<span class='label label-{'danger' if status == 'Fail' else 'success'}'>{status}</span>"
                        f"</a> "
                        f"<span class='glyphicon glyphicon-chevron-down'></span></div>"
                    )
                    html += (
                        f"<div id='collapse{panel_id}' class='panel-collapse "
                        f"collapse'>"
                    )
                    html += f"<div class='panel-body'>{detail}</div>"
                    if steps:
                        html += "<ul>"
                        for step, step_status in steps.items():
                            step_label_class = (
                                "danger" if step_status == "Fail" else "success"
                            )
                            html += (
                                f"<li>{step} - <span class='label label-{step_label_class}'>{step_status}</span"
                                f"></li>"
                            )
                        html += "</ul>"
                    if comment:
                        html += f"<div class='comment'>{comment}</div>"
                    html += "</div></div>"

                html += "</div></div>"

            html += "</div></div>"

        html += """
                <div id="statusModal" class="modal fade" role="dialog">
                    <div class="modal-dialog">
                        <div class="modal-content">
                            <div class="modal-body">
                                <input type="text" id="inputText" class="form-control" placeholder="Enter your text here...">
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-primary" onclick="saveLink()">Save</button>
                                <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                            </div>
                        </div>
                    </div>
                </div>
                <style>
                    .modal-content {
                        background-color: #fefefe;
                        margin: 15% auto;
                        padding: 20px;
                        border: 1px solid #888;
                        width: 80%;
                    }
                </style>
            </div>
        </body>
        </html>
                """
        return html

    def save_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(self.generate_html())
