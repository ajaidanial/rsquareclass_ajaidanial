// States 1,2,3,4,5
let curr_state = 1;
let course_num=0;
let master_object = {};
master_object["student"] = {
    'first_name': '',
    'last_name': '',
    'gender': '',
    'category': '',
    'aadhar': '',
    'dob': '',
    'address': '',
    'landmark': '',
    'city': '',
    'state': '',
    'pincode': '',
    'pnone': '',
    'school': '',
    'email': '',
    'nationality': ''
}
master_object["guardian"] = {
    relation: '',
    'salutation': '',
    'first_name': '',
    'last_name': '',
    'aadhar': '',
    'phone': '',
    'email': '',
    'occupation': ''
}
master_object["course"] = {
    'admission_date': '',
    'courses': [
        {
            'academic_year': '',
            'course_id': '',
            'quantity': ''
        }
    ],
    'additional_fee': [
        {
            'amount': '',
            'remarks': '',
        }
    ],
    'discount': {
        'type': '',
        'amount': ''
    },
    'notes': ''
}
master_object["payment"] = [
    {
        'amount': 'Rs. 20,000',
        'due_on': '26 Jan 2020',
        'created_by': 'Priyanka Trivedi',
        'created_on': '26 Dec. 2019',
        'status': 'UNPAID',
    }
]

$('#next-button').on("click", function(){
    state_update();
})

let state_update = () => {
    handle_state();
    initialize_state();
}

const studentDetailsStateHandler = () => {
    $('#student-add-form').parsley().whenValidate({group: 'student-details'}).done(function(){
    curr_state++;
    $('[href="#guardian-details"]').tab('show');
    });
}

const guardianStateHandler = () => {
    $('#student-add-form').parsley().whenValidate({group: 'guardian-details'}).done(function(){
    curr_state++;
    $('[href="#course-details"]').tab('show');
    master_object['guardian'] = {
        'relation': $('[name="guardian-relation"]').val(),
        'salutation': $('[name="guardian-salutation"]').val(),
        'first_name': $('#guardian-first-name').val(),
        'last_name': $('#guardian-last-name').val(),
        'aadhar': $('#guardian-aadhar').val(),
        'phone': $('#guardian-phone').val(),
        'email': $('#guardian-email').val(),
        'occupation': $('#guardian-occupation').val()
    }
    console.log(master_object);
    });
}

const courseStateHandler = () =>{
    $('#student-add-form').parsley().whenValidate({group: 'course-details'}).done(function(){
        $('#course-details').off("click", '.delete_course')
        $('#course-details').off("change", ":input")
        master_object['course']['admission_date'] = $('#admission-date').val();
        master_object['course']['courses'] = [];
        master_object['course']['additional_fee'] = [];
        $('tr[data-course-count]').each(function(){
            master_object['course']['courses'].push({
                'academic_year': $(this).find('[name="course_academic_year"]').val(),
                'course_id': $(this).find('[name="course-taken"]').val(),
                'quantity': $(this).find('[name="course_count"]').val()
            });
        })
        $('tr.extra-fee-row').each(function(){
            master_object['course']['additional_fee'].push({
                'remarks': $(this).find('[name="extra_fee_remarks"]').val(),
                'amount': $(this).find('[name="extra_fee"]').val()
            });
        })
        master_object["course"]["discount"] = {
            'type': $('[name="discount_type"]').val(),
            'amount': $('[name="discount"]').val()
        }
        master_object["course"]["notes"] = $('[name="notes"]').val();
        console.log(master_object);
    })
}

const handle_state = () => {
    switch(curr_state){
        case 1:        
        studentDetailsStateHandler();
        break;
        case 2:
        guardianStateHandler();
        break;
        case 3:
        courseStateHandler();
        break;
        
    }
}

const initialize_state = () => {
    switch(curr_state){
        case 1:
        $('#student-dob').bootstrapMaterialDatePicker({ weekStart : 0, time: false });        
        break;
        case 2:
        break;
        case 3:
        $('#admission-date').bootstrapMaterialDatePicker({ weekStart : 0, time: false });
        if(course_num==0){
            $('#add-course').trigger('click');
        }
        $('#course-details').on("click", '.delete_course', function(){
            $(this).closest('tr').remove();
            updateValues();
        })
        $('#course-details').on("change", ":input", function(){
            updateValues();
        })
        
        
        break;
        
    }
}

const updateValues = () => {
    let total_course_fee=0;
    let total_fee=0;
    $('tr[data-course-count]').each(function(){
        let curr_value = $(this).find('.course_count').val() * $(this).find('option:selected').attr('data-cost');
        total_course_fee += curr_value;
        $(this).find('[name=course_value]').val(curr_value);
    });
    $("input[name='extra_fee']").each(function(){
        if($(this).val()){
            total_course_fee = total_course_fee + parseInt($(this).val());
        }            
    })
    $('input[name="total_course_fee"]').val(total_course_fee);
    total_fee += total_course_fee;
    let discount_type = 'flat';
    if($('select[name="discount_type"]').val()=='flat'){
        discount_type = 'flat';
        $('.prepend-discount').text('Rs.')
    }else{
        discount_type="per";
        $('.prepend-discount').text('%')
    }
    let discount = $('[name="discount"]').val();
    if(discount_type=='flat'){
        total_fee -= discount
    }else{
        total_fee = total_fee - discount*total_fee/100;
    }
    $('[name="total-fee"').val(total_fee);        
    
}

const handleStudentDetailsData = () => {
    
}

$(document).ready(function(){
    initialize_state(1);
})


// let course_num=0;

// $('#add-course').on("click", function(){
//     course_num++;
//     $('#course-container tbody').append(`
//     <tr data-course-count="${course_num}">
//     <td>
//     <input type="text" name="course_academic_year" class="form-control" placeholder="2018-19">
//     </td>
//     <td>
//     <select class="form-control" name="course-taken">
//     {% for course in courses %}
//     <option val="{{course.id}}" data-cost="{{course.fee}}">{{course.name}}</option>
//     {% endfor %}
//     </select>
//     </td>
//     <td>
//     <input class="course_count" type="text" value="1" name="course_count">
//     </td>
//     <td>
//     <div class="input-group">
//     <div class="input-group-prepend">
//     <span class="input-group-text" id="basic-addon1">Rs.</span>
//     </div>
//     <input type="number" name="course_value" class="form-control" val="0" readOnly>
//     </div>
//     </td>
//     <td>
//     <a class="btn btn-light delete_course"><i class="mdi mdi-delete"></i></a>
//     </td>
//     </tr>
//     `);
//     $('tr[data-course-count="'+course_num+'"] .course_count').TouchSpin({
//         initval: 1,
//         buttondown_class: 'btn btn-primary',
//         buttonup_class: 'btn btn-primary'
//     });

//     rebindInputs();
// })

// rebindInputs = () => {
//     $('.delete_course').off('click');
//     $('.delete_course').on("click", function(){
//         $(this).closest('tr').remove();
//         updateValues();
//     })
//     $('#course-details :input').off("change");
//     $('#course-details :input').on("change", function(){
//         updateValues();
//     })
//     updateValues();
// }

// updateValues = () => {
//     let total_course_fee=0;
//     let total_fee=0;
//     $('tr[data-course-count]').each(function(){
//         let curr_value = $(this).find('.course_count').val() * $(this).find('option:selected').attr('data-cost');
//         total_course_fee += curr_value;
//         $(this).find('[name=course_value]').val(curr_value);
//     });
//     $("input[name='extra_fee']").each(function(){
//         if($(this).val()){
//             total_course_fee = total_course_fee + parseInt($(this).val());
//         }            
//     })
//     $('input[name="total_course_fee"]').val(total_course_fee);
//     total_fee += total_course_fee;
//     let discount_type = 'flat';
//     if($('select[name="discount_type"]').val()=='flat'){
//         discount_type = 'flat';
//         $('.prepend-discount').text('Rs.')
//     }else{
//         discount_type="per";
//         $('.prepend-discount').text('%')
//     }
//     let discount = $('[name="discount"]').val();
//     if(discount_type=='flat'){
//         total_fee -= discount
//     }else{
//         total_fee = total_fee - discount*total_fee/100;
//     }
//     $('[name="total-fee"').val(total_fee);        

// }

// $('#add-course').trigger("click");
// $('#additional-fee').on("click", function(){
//     $('#course-details tfoot').prepend(`
//     <tr>
//     <td></td>
//     <td class="text-right">Additional Fee</td>
//     <td>
//     <input type="text" name="extra_fee_remarks" class="form-control" placeholder="Remarks">
//     </td>
//     <td>
//     <div class="input-group">
//     <div class="input-group-prepend">
//     <span class="input-group-text" id="basic-addon1">Rs.</span>
//     </div>
//     <input type="number" name="extra_fee" class="form-control" val="0">
//     </div>
//     </td>
//     <td>
//     <a class="btn btn-light delete_course"><i class="mdi mdi-delete"></i></a>
//     </td>
//     </tr>
//     `);
//     rebindInputs();
// })