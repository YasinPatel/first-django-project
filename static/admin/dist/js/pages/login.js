$("#login-form").validate({
        errorElement: 'label', //default input error message container
        errorClass:'login-custom-error',
        focusInvalid: true, // do not focus the last invalid input
        rules: {
            username:{
                required:true,
              },
            password:{
                required:true,
              }
            },
        unhighlight: function(element) {
            var id_attr = $(element).parent('div').siblings('label');
            $(id_attr).remove();
        },	
		success: function (label)
        {
            label.closest('.form-group').removeClass('has-error'); // set success class to the control group
        },
				
        errorPlacement: function (error, element)
        {
            
            var parent_element = element.parent('div');
            error.insertAfter(parent_element);
        },
});

$("#reset-form").validate({
        errorElement: 'label', //default input error message container
        errorClass:'login-custom-error',
        focusInvalid: true, // do not focus the last invalid input
        rules: {
            email:{
                required:true,
                email:true,
              }
            },
        
		success: function (label)
        {
            label.closest('.form-group').removeClass('has-error'); // set success class to the control group
        },
				
        errorPlacement: function (error, element)
        {
            
            var parent_element = element.parent('div');
            error.insertAfter(parent_element);
        },
});

