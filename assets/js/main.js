// $("#id_btn").on("click", function (){
//     alert(1)
// })

// $(document).on("keyup", function (e){
//     alert(e.which)
// })
//
// $("id_btn").on("click", function (){
//     $("#id_div").html("dunyo")
// })
//
// $("#id_btn").on("click", function (){
//     $(".id_div").html("dunyo")
// })
// $("#id_btn").on("click", function (){
    // $("body").addClass("bg-danger")
    // setTimeout(function (){
    //     $("body").removeClass("bg-danger")
    // },  2000)

    // let d = $("<div />").addClass("alert alert-success").html("Salom Dunyo")
    // alert(d[0].outerHTML)
    // $("#id_btn").appendTo("body")
    // d.prependTo("body")
    // d.prependTo("#id_container")
    // $("#id_container").prepend(d)
    // $("#id_container").append(d)
    // $("#id_container").css("background", "red")
// })
// $(".cat-link").on("click", function (){
//     // $('#id_content').html($(this).attr("href"))
//     let catname = $(this).find(".cat-name").html()
//     let catid = $(this).data("id")
//     // let catname = $(this).attr("data-title")
//     // let catname = $(this).data("title")
//     let imagelink = $(this).find(".cat-img").css("background-image")
//     let image = $("<div />").attr("style", imagelink).css("width", "50px").css("height", "50px")
//     let h1 = $("#id_content > h1").first()
//     if (h1.length >0) {
//         // h1.html(catname)
//
//
//         h1.html("<div style='" + imagelink + "'/>" + catname)
//         alert(h1);
//
//     }
//     else{
//         let header = $("<h1 />").addClass("text-muted mt-3").html(catname)
//         header.prependTo("#id_content")

//     }
//
//     // alert($(this).data("id"));
//
//
//     // $("#id_content").html(header)
//     function append_result(result){
//         $("#id_content > h1").nextAll().remove()
//         $("#id_content").append(result)
//
//         $("#id_content .pagination a.page-link").on("click", function (){
//             let a_href = $(this).attr("href")
//             let params = new URLSearchParams(a_href)
//             let page = params.get('page', 1)
//             $.ajax({
//                     method: 'get',
//                     url: '/uz/cat-ajax/' + catid + "/",
//                     data: {page: page},
//                     success: function (result){
//                        // $("#id_content").html(result)
//                         append_result(result)
//                     }
//                 })
//             return false
//         })
//     }
//     // append_result("<img src='/static/img/loading.gif'/>")
//
//
//     $.ajax({
//     method: 'get',
//     url: '/uz/cat-ajax/' + catid + "/",
//     data: {page: page},
//     success: function (result){
//
//        // $("#id_content").html(result)
//         append_result(result)
//     }
// })
//
//
//
//     return false;
// })
// $(".cat-link").on("click", function (){
//
//     alert(imagelink);
//
//     return false
// })

$(".cat-link").on("click", function (){
    let catname = $(this).find(".cat-name").html()
    let catid = $(this).data("id")
    // let imagelink = $(this).find(".cat-image").css('background-image')
    // let image = $('<div />').css("background-image", imagelink).css('width', '50px').css('height', '50px')
    let h1 = $("#id_content > h1").first()
    if (h1.length >0) {
        // h1.html(image + catname)
        h1.html(catname)
        // alert(imagelink)

    }
    else{
        let header = $("<h1 />").addClass("text-muted mt-3").html(catname)
        header.prependTo("#id_content")
    }

    function append_result(result){
        $("#id_content > h1").nextAll().remove()
        $("#id_content").append(result)

        $("#id_content .pagination a.page-link").on('click', function (){
            let a_href = $(this).attr('href')
            let params = new URLSearchParams(a_href)
            let page = params.get('page', 1)

            make_query(page)
            return false
        })
    }

    function make_query(page=1){
        append_result("</img src='/static/img/loading.gif'/>")

        let lang = window.location.href.split('/')[3]

        $.ajax({
            method: 'get',
            url: '/' + lang + '/cat-ajax/' + catid + "/",
            data: {page: page},
            success: function (result){
                append_result(result)
            }
        })
    }

    make_query()

    return false;
})

