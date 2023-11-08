"""
python report to html
"""


class TestReport:
    def __init__(self):
        self.app_version = ""
        self.device_version = ""
        self.categories = {
            "vlauncher": {},
            "STB": {},
            "wallpaper": {},
            "authenticator": {},
            "quicksettings": {},
            "screenlock": {},
        }

    def add_entry(self, report_data):
        if report_data.subcategory not in self.categories[report_data.category]:
            self.categories[report_data.category][report_data.subcategory] = []
        self.categories[report_data.category][report_data.subcategory].append(
            (
                report_data.testcase,
                report_data.detail,
                report_data.steps,
                report_data.status,
            )
        )

    def add_version_info(self, model, fw_version, app_version):
        self.device_version = [
            f"Model: {model}",
            f"FW version: {fw_version}",
        ]
        self.app_version = app_version
        return self.device_version, self.app_version

    def generate_html(self):
        # html temp
        html_head = f"""<html> <head> <title>Automation Test Report</title> <link href="./html_css/bootstrap.min.css" 
        rel="stylesheet"> <script src="./html_css/jquery.min.js"></script><script 
        src="./html_css/bootstrap.min.js"></script><script src="./html_css/filter.js"></script> <style> #summary {{ 
        font-size: 20px; }} #summary-card .card-body {{ margin-bottom: 0; }} #device-version .list-group-item {{ 
        border: none; }} #device-version table {{ width: 100%; }} #device-version table th, #device-version table td 
        {{ padding: 12px; text-align: left; border: 1px solid #ddd; }} #device-version table th {{ background-color: 
        #f2f2f2; }} </style> </head> <body> <div class="container"> <h1 class='text-center'>Automation Test 
        Report</h1>  <div id="summary-card" class="card"> <div class="card-body"> <div id="device-version" 
        class="text-center alert summary-alert"> <table class="table"> <thead> <tr> <th>Device Information</th> </tr> 
        </thead> <tbody>"""

        # 逐行将 device_version 中的每个信息添加到 HTML 表格中
        for _ in self.device_version:
            html_head += f"<tr><td>{_}</td></tr>"
        html_head += """</tbody>
                </table>
                <table class="table">
                    <thead>
                        <tr>
                            <th colspan="2">App Information</th>
                        </tr>
                    </thead>
                    <tbody>"""

        # 逐行将 device_version 中的每个信息添加到 HTML 表格中
        for i, _ in enumerate(self.app_version):
            # 使用 i 来确定是第一列还是第二列
            column_index = i % 2
            if column_index == 0:
                html_head += "<tr>"
            html_head += f"<td>{_}</td>"
            if column_index == 1:
                html_head += "</tr>"
        html_head += """</tbody> </table> </div> <div id="summary" class="text-center alert summary-alert"></div> 
        </div> </div> <div class="text-center"> <button id="allButton" class="btn btn-default">All</button> <button 
        id="passButton" class="btn btn-success">Pass</button> <button id="failButton" class="btn 
        btn-danger">Fail</button></div> <br>"""

        html_report = self.generate_report_html()

        html_end = """<div id="statusModal" class="modal fade" role="dialog"> 
        <div class="modal-dialog"> <div class="modal-content"> <div class="modal-body"> 
        <input type="text" id="inputText" class="form-control" placeholder="Enter your text here..."> </div> 
        <div class="modal-footer"> <button type="button" class="btn btn-primary" onclick="save_link()">Save</button> 
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

        for idx, (testcase, detail, steps, status) in enumerate(testcases):
            panel_id = f"{safe_category_id}_{safe_subcategories_id}_{idx}"
            subcategory_html += self.generate_testcase_html(
                panel_id, testcase, detail, steps, status
            )

        subcategory_html += "</div></div>"
        return subcategory_html

    @staticmethod
    def generate_testcase_html(panel_id, testcase, detail, steps, status):
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
        testcase_html += "</div></div>"

        return testcase_html

    @staticmethod
    def get_pass_and_total_count(testcases):
        pass_count = sum(1 for _, _, _, status, in testcases if status == "Pass")
        total_count = len(testcases)
        return pass_count, total_count

    def save_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            file.write(self.generate_html())
