$(function() {
    // Get the price_per variable from the global Django JavaScript object
    var pricePer = django.jQuery('#price_per').val();
  
    // Hide or show fields based on the pricePer variable
    if (pricePer == 'Per_Person') {
      django.jQuery('#id_Total_Product, #id_Product_Price').hide();
      django.jQuery('#id_Per_Adults_Price, #id_Per_Child_Price, #id_Per_Infant_Price').show();
    } else {
      django.jQuery('#id_Per_Adults_Price, #id_Per_Child_Price, #id_Per_Infant_Price').hide();
      django.jQuery('#id_Total_Product, #id_Product_Price').show();
    }
  
    // Bind an event listener to the price_per field to update the hidden fields when the user changes the value
    django.jQuery('#id_Price_Per').on('change', function() {
      var pricePer = django.jQuery(this).val();
  
      if (pricePer == 'Per_Person') {
        django.jQuery('#id_Total_Product, #id_Product_Price').hide();
        django.jQuery('#id_Per_Adults_Price, #id_Per_Child_Price, #id_Per_Infant_Price').show();
      } else {
        django.jQuery('#id_Per_Adults_Price, #id_Per_Child_Price, #id_Per_Infant_Price').hide();
        django.jQuery('#id_Total_Product, #id_Product_Price').show();
    }
});
});
