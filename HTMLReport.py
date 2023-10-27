"""
python report to html
"""


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
        # html temp
        html_head = """<html> <head> <title>Automation Test Report</title> <link href="./html_css/bootstrap.min.css" 
        rel="stylesheet"> <script src="./html_css/jquery.min.js"></script><script 
        src="./html_css/bootstrap.min.js"></script><script src="./html_css/filter.js"></script> <style> #summary { 
        font-size: 20px; } </style> </head> <body> <div class="container"> <h1 class='text-center'>Automation Test 
        Report</h1> <div class="text-center"> <button onclick="filterTestCases('all')" class="btn 
        btn-default">All</button> <button onclick="filterTestCases('pass')" class="btn btn-success">Pass</button> 
        <button onclick="filterTestCases('fail')" class="btn btn-danger">Fail</button> <div id="summary-card" 
        class="card"> <div class="card-body"> <div id="summary" class="text-center alert summary-alert"></div> </div> 
        </div> </div> <br>"""

        html_report = self.generate_report_html()

        html_end = """<div id="statusModal" class="modal fade" role="dialog"> 
        <div class="modal-dialog"> <div class="modal-content"> <div class="modal-body"> 
        <input type="text" id="inputText" class="form-control" placeholder="Enter your text here..."> </div> 
        <div class="modal-footer"> <button type="button" class="btn btn-primary" onclick="saveLink()">Save</button> 
        <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button> </div> 
        </div> </div> </div> <style> .modal-content { background-color: #fefefe; margin: 15% auto; padding: 20px; 
        border: 1px solid #888; width: 80%; } </style> </div> </body> </html>"""

        html = f"{html_head}{html_report}{html_end}"
        return html

    def generate_report_html(self):
        report_html = ""
        for category, subcategories in self.categories.items():
            safe_category_id = category.replace(" ", "_").replace("-", "_")
            report_html += self.generate_category_html(
                category, safe_category_id, subcategories
            )
        return report_html

    def generate_category_html(self, category, safe_category_id, subcategories):
        category_html = f"<div class='panel panel-primary category-panel' id='category_{safe_category_id}'>"
        category_html += (
            f"<div class='panel-heading' data-toggle='collapse' "
            f"href='#collapse{safe_category_id}'>{category} "
            f"<span class='glyphicon glyphicon-chevron-down'></span></div>"
        )
        category_html += (
            f"<div id='collapse{safe_category_id}' class='panel-collapse collapse in'>"
        )

        for subclass, testcases in subcategories.items():
            safe_subcategories_id = subclass.replace(" ", "_").replace("-", "_")
            pass_count, total_count = self.get_pass_and_total_count(testcases)
            category_html += self.generate_subcategory_html(
                safe_category_id,
                safe_subcategories_id,
                subclass,
                pass_count,
                total_count,
                testcases,
            )

        category_html += "</div></div>"
        return category_html

    def generate_subcategory_html(
        self,
        safe_category_id,
        safe_subcategories_id,
        subclass,
        pass_count,
        total_count,
        testcases,
    ):
        subcategory_html = (
            f"<div class='panel panel-info subcategory-panel' "
            f"id='category_{safe_category_id}_{safe_subcategories_id}'>"
        )
        subcategory_html += (
            f"<div class='panel-heading' data-toggle='collapse' "
            f"href='#collapse{safe_category_id}_{safe_subcategories_id}'>"
            f"{subclass} ({pass_count}/{total_count}) "
            f"<span class='glyphicon glyphicon-chevron-down'></span></div>"
        )
        subcategory_html += (
            f"<div id='collapse{safe_category_id}_{safe_subcategories_id}' class='panel-collapse collapse "
            f"in'>"
        )

        for idx, (testcase, detail, steps, status, comment) in enumerate(testcases):
            panel_id = f"{safe_category_id}_{safe_subcategories_id}_{idx}"
            subcategory_html += self.generate_testcase_html(
                panel_id, testcase, detail, steps, status, comment
            )

        subcategory_html += "</div></div>"
        return subcategory_html

    @staticmethod
    def generate_testcase_html(panel_id, testcase, detail, steps, status, comment):
        testcase_html = f"<div class='panel panel-default test-case {status.lower()}'>"
        testcase_html += (
            f"<div class='panel-heading' data-panel-id='{panel_id}' data-toggle='collapse' "
            f"href='#collapse{panel_id}'>"
            f"{testcase} - "
            f"<span class='status-link label label-{'danger' if status == 'Fail' else 'success'}'>{status}</span>"
            f"<a href='javascript:void(0);' id='comment-link' target='_blank'></a>"
            f"<span class='glyphicon glyphicon-chevron-down'></span>"
            f"<span class='comment-display' id='comment_{panel_id}'></span></div>"
        )
        testcase_html += (
            f"<div id='collapse{panel_id}' class='panel-collapse " f"collapse'>"
        )
        testcase_html += f"<div class='panel-body'>{detail}</div>"
        if steps:
            testcase_html += "<ul>"
            for step, step_status in steps.items():
                step_label_class = "danger" if step_status == "Fail" else "success"
                testcase_html += (
                    f"<li>{step} - <span class='label label-{step_label_class}'>{step_status}</span"
                    f"></li>"
                )
            testcase_html += "</ul>"
        if comment:
            testcase_html += f"<div class='comment'>{comment}</div>"
        testcase_html += "</div></div>"

        return testcase_html

    @staticmethod
    def get_pass_and_total_count(testcases):
        pass_count = sum(1 for _, _, _, status, _ in testcases if status == "Pass")
        total_count = len(testcases)
        return pass_count, total_count

    def save_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(self.generate_html())
