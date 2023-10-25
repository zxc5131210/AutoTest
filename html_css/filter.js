// js of report to html
function updateSummary() {
    const totalTestCases = $(".test-case").length;
    const passedTestCases = $(".test-case.pass").length;
    const failedTestCases = $(".test-case.fail").length;

    const passPercentage = (passedTestCases / totalTestCases) * 100;
    const failPercentage = (failedTestCases / totalTestCases) * 100;

    // update summary
    $("#summary").html(`
        <p>Summary: ${passedTestCases}/${totalTestCases}</p>
        <p>Passed: ${passedTestCases} (${passPercentage.toFixed(2)}%)</p>
        <p>Failed: ${failedTestCases} (${failPercentage.toFixed(2)}%)</p>
    `);
}

function openPopup(status, panelId) {
    $('#statusModal').modal('show');
    $('#statusModal').data('panelId', panelId);

    // Retrieve and display saved comment for this panelId
    var savedComment = localStorage.getItem(panelId);
    $('#inputText').val(savedComment);
}

function saveLink() {
    var panelId = $('#statusModal').data('panelId');
    var inputText = $('#inputText').val();

    // Save the comment to local storage
    localStorage.setItem(panelId, inputText);

    // Update the link in real-time
    updateLink(panelId, inputText);

    $('#statusModal').modal('hide');
}

function updateLink(panelId, comment) {
    var statusElement = $('#' + panelId).find('.panel-heading .label');
    var link = $('<a>').attr('href', 'javascript:void(0)').text(' ' + comment).addClass('label label-info');

    // Remove any previous links
    statusElement.next('a').remove();

    if (comment) {
        statusElement.after(link);
    }
}

// Restore saved information on page load
$(document).ready(function () {
    loadComments();
});

// Clear all saved information (for testing purposes)
function clearSavedInfo() {
    localStorage.clear();
    loadComments();
}

// Update the link in real-time as the user types
$('#inputText').on('input', function () {
    const panelId = $('#statusModal').data('panelId');
    const inputText = $(this).val();
    updateLink(panelId, inputText);
});

function loadComments() {
    $(".test-case").each(function () {
        var panelId = $(this).find('.panel-heading').attr('id');
        var savedComment = localStorage.getItem(panelId);
        if (savedComment) {
            updateLink(panelId, savedComment);
        }
    });
}

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

    updateSummary();
}


// Ensure filterTestCases is called on document ready and button click
$(document).ready(function () {
    // Bind the filterTestCases function to the filter buttons
    $(".filter-button").click(function () {
        filterTestCases($(this).data("filter-type"));
    });
    $('#id_of_save_button').click(saveLink);

    // Default display
    filterTestCases("all");
    updateSummary();
});
