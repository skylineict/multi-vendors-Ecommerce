
$('.button-add-to-cart').on('click', function(){
    let button = $(this);
    _index=button.attr('data-index')
    let price = $(".current-product-price-"+_index).text();
    let qty = $(".product-quantity-"+_index).val();
    let productid = $(".product-id-"+_index ).val();
    let product_name =  $(".product-name-"+_index).val();
    let product_image = $(".product-image-"+_index).val();
    let product_pid =  $(".product-pid-"+_index).val();
  

    // console.log(index);
    console.log('index', _index);
    console.log('price', price);
    console.log('image',product_image)
    console.log('quantiy',qty)
    console.log('product', product_name )
    // console.log('price', price)
    console.log('id', productid);
    console.log('product_pid', product_pid);
    // console.log('button', button);

    $.ajax({
        url: '/product_list/add-to-cart',
        data: {
            'id': productid,
            'qty': qty,
            'price': price,
            'product_name': product_name,
            'image': product_image,
            'product_pid':product_pid
        },
        dataType: 'json',
        beforeSend: function() {
            button.attr('disabled', true)
            
        },
        success: function(res) {
            
            button.html('<i class="fa fa-check" aria-hidden="true"></i>');
            $('#cart-item-count').text(res.total_item)
            button.attr('disabled', false)
           
        },
        error: function(err) {
            console.error('Error adding item:', err);
        }
    });
});





// here is ajax code that delete item from cart
$(document).on("click", '.removed-product', function()
{
    let removedid = $(this).attr('data-product')
    let btn =  $(this)
    console.log(removedid)
    $.ajax({
         url: '/product_list/delete_product_cart',
        data:{
            'id': removedid
        },

        dataType: 'json',

        beforeSend:function(){
            btn.hide()

        },

        success:  function(res){
            btn.show()
            $('#cart-item-count').text(res.total_item),
            $('#cart-list').html(res.data)
 },
   })   
})





$(document).on("click", '.update-product', function()
{
    let product_id = $(this).attr('data-update')
    let product_quantity = $('.quantiy-product-' + product_id).val()
    let btn =  $(this)
    console.log("product id:" +product_id)
    console.log("product quantity:" + product_quantity)
    $.ajax({
         url: '/product_list/update_cart_item',
        data:{
            'id': product_id,
            'qty':product_quantity
        },

        dataType: 'json',

        beforeSend:function(){
            btn.hide()
            console.log('it is not working')

        },

        success:  function(res){
            btn.show()
            console.log('e done work ')
            $('#cart-item-count').text(res.total_item),
            $('#cart-list').html(res.data)
 },
   })   
})






















// $('#button-add-to-cart').on('click', function(){

//     let price = $('#current-product-price').text();
//     let qty =  $('#product-quantity').val();
//     let productid =  $('#product-id').val();
//     let product_name =  $('#product_title').val();
//     let button = $(this);

//     console.log('current-price', price);
//     console.log('qty', qty);
//     console.log('product_id', productid);
//     console.log('product_name', product_name);
//     console.log('button', button);

//     $.ajax({
//         url: '/product_list/add-to-cart',
//         data: {
//             'id': productid,
//             'qty': qty,
//             'price': price,
//             'product_name': product_name
//         },
//         dataType: 'json',
//         beforeSend: function() {
//             button.attr('disabled', true)
            
//         },
//         success: function(res) {
            
//             button.html('Item added <i class="fa fa-check" aria-hidden="true"></i>');
//             $('#cart-item-count').text(res.total_item)
//             button.attr('disabled', false)
//             button.html('add to cart ');
//         },
//         error: function(err) {
//             console.error('Error adding item:', err);
//         }
//     });
// });
