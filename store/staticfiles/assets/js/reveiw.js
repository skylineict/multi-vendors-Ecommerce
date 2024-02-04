let sucess = $('.mymessage').hide()

var currentDate = new Date();

// You can format the date as needed
var formattedDate = currentDate.toISOString().slice(0, 10);


$('#commentForm').submit(function (event) {


    event.preventDefault();

    $.ajax({

        data: $(this).serialize(),
        method: $(this).attr('method'),
        url: $(this).attr('action'),
        datatype: 'json',
        success: function (res) {
            if (res.bool == true) {
                $('.mymessage').html('Review created sucessfully')
                $('.mymessage').show()

                // this code make the form to disapper
                setTimeout(() => {
                    $('.mymessage').alert('close')
                }, 3000)

                $('.comment-form').hide('')


                let user_review = '<div class="single-comment justify-content-between d-flex mb-30">'
                user_review += '<div class="user justify-content-between d-flex">'
                user_review += '<div class="thumb text-center">'
                user_review += '<img src="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png" alt="" />'
                user_review += '<a href="#" class="font-heading text-brand">' + res.context.user + '</a>'
                user_review += '</div>'


                user_review += '<div class="desc">'
                user_review += '<div class="justify-content-between mb-10">'
                user_review += '<div class="d-flex align-items-center">'
                user_review += '<span class="font-xs text-muted">' + formattedDate + '</span>'
                user_review += '</div>'



                for (let i = 1; i <= res.context.rating; i++) {

                    user_review += '<i class="fas fa-star text-warning"> </i>';


                }


                user_review += '<p class="mb-10">' + res.context.comment + '</p>'

                user_review += '</div>'
                user_review += '</div>'
                user_review += '</div>'


                $('.comment-list').prepend(user_review)


            } else {

                console.log('this stuff is not working')

            }
        }
    });

});