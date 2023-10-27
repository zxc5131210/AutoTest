// -----------------
// Helper Functions
// -----------------
function update_summary() {
    const total_test_case = $(".test-case").length;
    const passed_test_cases = $(".test-case.pass").length;
    const failed_test_case = $(".test-case.fail").length;
    const pass_rate = (passed_test_cases / total_test_case) * 100;
    const fail_rate = (failed_test_case / total_test_case) * 100;

    $("#summary").html(`
        <p>Summary: ${passed_test_cases}/${total_test_case}</p>
        <p>Passed: ${passed_test_cases} (${pass_rate.toFixed(2)}%)</p>
        <p>Failed: ${failed_test_case} (${fail_rate.toFixed(2)}%)</p>
    `);
}
function update_element(panelId, comment) {
    const statusElement = $(`div[data-panel-id="${panelId}"]`).find('.label');
    const existingLink = statusElement.siblings('.comment-link');

    if (existingLink.length) {
        existingLink.attr('href', comment).text(' ' + comment);
    } else {
        const commentLink = $('<a>')
            .attr('href', comment)
            .attr('target', '_blank')
            .text(' ' + comment)
            .addClass('comment-link');
        statusElement.after(commentLink);
    }

    // Re-bind the click event for comment-link
    $('.comment-link').off('click').on('click', function(event) {
        event.preventDefault();  // 阻止連結的默認行為
        event.stopPropagation();  // 阻止事件冒泡
        window.open($(this).attr('href'), '_blank');
    });

    // Re-bind the click event for panel-heading
    $(".panel-heading").off("click").on("click", function(event) {
        if (!$(event.target).hasClass("comment-link") && !$(event.target).closest(".comment-link").length) {
            const collapseElement = $(this).next();
            collapseElement.collapse('toggle');
        }
    });
}

function open_popup(status, panelId) {
    $('#statusModal').modal('show');
    $('#statusModal').data('panelId', panelId);
    const saved_comment = localStorage.getItem(panelId);
    $('#inputText').val(saved_comment);
}
function filter_test_cases(filterType) {
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
            $(".subcategory").each(function () {
                if ($(this).find(".test-case.pass:not(.hidden)").length === 0) {
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
            $(".subcategory").each(function () {
                if ($(this).find(".test-case.fail:not(.hidden)").length === 0) {
                    $(this).addClass("hidden");
                }
            });
            break;
    }

    update_summary();
}

function bind_events() {
    // Re-bind the click event for comment-link
    $('.comment-link').off('click').on('click', function(event) {
        event.preventDefault();  // 阻止連結的默認行為
        event.stopPropagation();  // 阻止事件冒泡
        window.open($(this).attr('href'), '_blank');
    });

    // Re-bind the click event for panel-heading
    $(".panel-heading").off("click").on("click", function(event) {
        if ($(event.target).hasClass("label")) {
            console.log("Label was clicked!");  // 調試日誌
            const panelId = $(this).attr("data-panel-id");
            const status = $(event.target).text();
            open_popup(status, panelId);
        } else if (!$(event.target).hasClass("comment-link") && !$(event.target).closest(".comment-link").length) {
            console.log("Panel heading was clicked!");  // 調試日誌
            const collapseElement = $(this).next();
            collapseElement.collapse('toggle');
        }
    });
}
function toggleCollapse(elementId) {
    const x = document.getElementById(elementId);
    if (x.className.indexOf("in") == -1) {
        x.className += " in";
    } else {
        x.className = x.className.replace(" in", "");
    }
}

// -----------------
// Download HTML Functions
// -----------------
function download_html() {
    const updatedHTML = document.documentElement.outerHTML;
    const blob = new Blob([updatedHTML], {type: 'text/html'});
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'updated_report.html';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    bind_events();  // 在download_html結束時重新綁定事件
}

function save_link() {
    const panelId = $('#statusModal').data('panelId');
    const inputText = $('#inputText').val();
    update_element(panelId, inputText);
    $('#statusModal').modal('hide');
    setTimeout(download_html, 500);
}

// -----------------
// Event Handlers and Initializers
// -----------------
$(document).ready(function() {
    // Initial display on page load
    filter_test_cases("all");
    update_summary();

    // Event bindings
    $(".filter-button").click(function() {
        filter_test_cases($(this).data("filter-type"));
    });

    $('#id_of_save_button').click(save_link);

    $("body").on("click", ".status-link", function(event) {
        console.log("Status link clicked!");  // 調試日誌
        event.stopPropagation();
        const panelId = $(this).closest(".panel-heading").attr("data-panel-id");
        const status = $(this).find(".label").text();
        open_popup(status, panelId);
    });
    bind_events();  // 確保在文檔加載時綁定事件
});
