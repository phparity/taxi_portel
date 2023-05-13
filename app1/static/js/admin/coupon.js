window.onload = function() {
    // Get references to the relevant form elements
    var typeField = document.getElementById("id_Type");
    var percentageField = document.getElementById("id_Percentage");
    var quantityField = document.getElementById("id_Quantity");
    var limitField = document.getElementById("id_Limit");
    
    // Hide the Percentage and Limit fields initially
    percentageField.parentElement.parentElement.style.display = "none";
    limitField.parentElement.parentElement.style.display = "none";
    
    // Show or hide the Percentage and Limit fields based on the selected values of the Type and Quantity fields
    typeField.addEventListener("change", function() {
        if (typeField.value === "Discount By Percentage") {
            percentageField.parentElement.parentElement.style.display = "table-row";
        } else {
            percentageField.parentElement.parentElement.style.display = "none";
        }
    });
    
    quantityField.addEventListener("change", function() {
        if (quantityField.value === "Limited") {
            limitField.parentElement.parentElement.style.display = "table-row";
        } else {
            limitField.parentElement.parentElement.style.display = "none";
        }
    });
};