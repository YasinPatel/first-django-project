$(document).ready(function(){
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    
    $('body').on('click','#change-status',function(){
        var geturl = $(this).attr('data-url');
        var getid = $(this).attr('data-slug-id');
        var t = $(this);
        
        $.ajax({
            method:"POST",
            url:geturl,
            beforeSend: function(xhr, settings) {
                    if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                        // Only send the token to relative URLs i.e. locally.
                        xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                    }
            },
            data:{"data-id":getid},
            success:function(data){
                data = $.parseJSON(data);
                if (data['active'] == "yes") {
                    var render_button = "<a href='javascript:void(0);' data-slug-id='"+ data['data-slug-id'] +"' data-url='"+ data['data-url'] +"' id='change-status' class='label label-success' >Active</a>";
                    t.replaceWith(render_button);
                }
                else if (data['active'] == "no") {
                    var render_button = "<a href='javascript:void(0);' data-slug-id='"+ data['data-slug-id'] +"' data-url='"+ data['data-url'] +"' id='change-status' class='label label-danger' >Inactive</a>";
                    t.replaceWith(render_button)
                }
                else
                {
                    console.log('Else');
                }
            },
            erorr:function(){
                
            }
            
        })
    })
    
    
    $('body').on('click','#delete-status',function(){
        var geturl = $(this).attr('data-url');
        var getid = $(this).attr('data-slug-id');
        var t = $(this);
        
        swal({
            title: 'Are you sure?',
            text: "You won't be able to revert this!",
            type: 'warning',
            showCancelButton: true,
            confirmButtonColor: '#d33',
            cancelButtonColor: '#00acd6',
            confirmButtonText: 'Yes, delete it!',
          }).then(function () {
            $.ajax({
                    method:"POST",
                    url:geturl,
                    beforeSend: function(xhr, settings) {
                            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
                            }
                    },
                    data:{"data-id":getid},
                    success:function(data){
                        if (data == 'success') {
                            location.reload();
                        }
                    },
                    erorr:function(){
                        
                    }
                    
                })
          }, function (dismiss) {
                
            })
        
        
        //$.ajax({
        //    method:"POST",
        //    url:geturl,
        //    beforeSend: function(xhr, settings) {
        //            
        //            if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
        //                // Only send the token to relative URLs i.e. locally.
        //                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
        //            }
        //    },
        //    data:{"data-id":getid},
        //    success:function(data){
        //        location.reload();
        //    },
        //    erorr:function(){
        //        
        //    }
        //    
        //})
    })
    
})