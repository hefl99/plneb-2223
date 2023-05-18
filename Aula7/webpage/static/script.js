
$(document).ready(function () {
    $('#example').DataTable({
        autoWidth: false,
        columns: [
            { "width": "15%" },
            { "width": "15%" },
            { "width": "15%" },
            { "width": "15%" },
            { "width": "40%" }
        ]
    })
});

function deleteTerm(designation) {
    $.ajax("/term/"+designation, {
        type:"DELETE",
        success: function(data) {
            window.location.href = '/terms'
        }
    })
}