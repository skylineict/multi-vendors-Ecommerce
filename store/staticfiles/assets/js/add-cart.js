$('#button-add-to-cart').on('click', function(){

    let price = $('#current-product-price').text();
    let qty =  $('#product-quantity').val();
    let productid =  $('#product-id').val();
    let product_name =  $('#product_title').val();
    let button = $(this);

    console.log('current-price', price);
    console.log('qty', qty);
    console.log('product_id', productid);
    console.log('product_name', product_name);
    console.log('button', button);

    $.ajax({
        url: 'add-to-cart',
        data: {
            'id': productid,
            'qty': qty,
            'price': price,
            'product_name': product_name
        },
        dataType: 'json',
        beforeSend: function() {
            console.log('Adding item...');
        },
        success: function(res) {
            console.log('Item added successfully:', res);
            button.html('Item added <i class="fa fa-check" aria-hidden="true"></i>');
        },
        error: function(err) {
            console.error('Error adding item:', err);
        }
    });
});
