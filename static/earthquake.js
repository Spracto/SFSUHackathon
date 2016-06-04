"use strict";

$(function() {
      $("#submit").click( function()
           {
             var address = $('#address').val();
             console.log(address);

			$.ajax({
				url: '/address',
				data: address,
				type: 'GET',
				success: function(response) {
					console.log(response);
				},
				error: function(error) {
					console.log(error);
				}
			});
		}
);
});