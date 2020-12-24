window.onload = function () {
    $('#main-block').change(function() {
    var input = document.getElementById("amount_of_currency_from");
    var input_value = input.value;

    var from_currency = document.getElementById("from_currency");
    var from_currency_value = from_currency.value;

    var to_currency = document.getElementById("to_currency");
    var to_currency_value = to_currency.value;

    $.ajax({
        url: 'ajax/get_response/',
        data: {
          'input_value': input_value,
          'from_currency_value': from_currency_value,
          'to_currency_value' : to_currency_value
        },
        dataType: 'json',
        success: function (data) {
          document.getElementById('result').innerHTML = data.respond;
        }
      });
    });
};