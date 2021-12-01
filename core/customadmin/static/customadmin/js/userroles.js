/*global $ */
'use strict';

var userroles = {

    // ------------------------------------------------------------------------
    // Users
    // ------------------------------------------------------------------------
    users: {

        index: function () {
            $('#user-table').DataTable({
                pageLength: 25,
                responsive: true,
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },],

                // Ajax for pagination
                // processing: true,
                // serverSide: true,
                // ajax: {
                //     url: window.pagination_url,
                //     type: 'get',
                //     beforeSend: function(xhr) {                      
                //         xhr.setRequestHeader(
                //             "X-CSRFToken",
                //             $("input[name=csrfmiddlewaretoken]").val()
                //           );
                //     },
                // },
                // columns: [
                //     { data: 'username', name: 'username' },
                //     { data: 'first_name', name: 'first_name' },
                //     { data: 'last_name', name: 'last_name' },
                //     { data: 'is_superuser', name: 'is_superuser' },
                //     // { data: 'modified', name: 'modified' },
                //     { data: 'actions', name: 'actions' }
                // ],
            });

        },

        details: function () {
            $('.groups-select').bootstrapDualListbox({
                nonSelectedListLabel: 'Available groups',
                selectedListLabel: 'Chosen groups',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });

            $('.permissions-select').bootstrapDualListbox({
                nonSelectedListLabel: 'Available user permissions',
                selectedListLabel: 'Chosen user permissions',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });
        }

    },

    // ------------------------------------------------------------------------
    // Groups
    // ------------------------------------------------------------------------
    groups: {

        index: function () {
            $('#group-table').DataTable({
                pageLength: 25,
                responsive: true,
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },]
            });
        },

        details: function () {
            $('.permissions-select').bootstrapDualListbox({
                nonSelectedListLabel: 'Available user permissions',
                selectedListLabel: 'Chosen user permissions',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });
        }

    },

    // ------------------------------------------------------------------------
// ------------------------------------------------------------------------
    // Customers
    // ------------------------------------------------------------------------
    customers: {
        
        index: function () {
            $('#customer-table').DataTable({
                pageLength: 25,
                responsive: true,
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },],

                // Ajax for pagination
                // processing: true,
                // serverSide: true,
                // ajax: {
                //     url: window.pagination_url,
                //     type: 'get',
                // },
                // columns: [
                //     { data: 'username', name: 'username' },
                //     { data: 'first_name', name: 'first_name' },
                //     { data: 'last_name', name: 'last_name' },
                //     { data: 'is_superuser', name: 'is_superuser' },
                //     // { data: 'modified', name: 'modified' },
                //     { data: 'actions', name: 'actions' }
                // ],
            });

        },

        details: function () {
            $('.groups-select').bootstrapDualListbox({
                nonSelectedListLabel: 'Available groups',
                selectedListLabel: 'Chosen groups',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });

            $('.permissions-select').bootstrapDualListbox({
                nonSelectedListLabel: 'Available user permissions',
                selectedListLabel: 'Chosen user permissions',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });
            $('#id_birth_date').daterangepicker({
                singleDatePicker: true,
                locale: {
                    format: 'YYYY-MM-DD'
                }
            });
        }

    },
    // Customers
    // ------------------------------------------------------------------------
    categories: {

        index: function () {
            $('#category-table').DataTable({
                pageLength: 25,
                responsive: true,
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },],

                // Ajax for pagination
                processing: true,
                serverSide: true,
                ajax: {
                    url: window.pagination_url,
                    type: 'get',
                    beforeSend: function(xhr) {                      
                        xhr.setRequestHeader(
                            "X-CSRFToken",
                            $("input[name=csrfmiddlewaretoken]").val()
                          );
                    },
                },
                columns: [
                    { data: 'name', name: 'name' },
                    { data: 'image', name: 'image' },
                    { data: 'status', name: 'status' },
                    { data: 'actions', name: 'actions' },
                ],
            });

        },

    },
    // Customeraddresss
    // ------------------------------------------------------------------------
    customeraddresses: {

        index: function () {
            $('#customeraddress-table').DataTable({
                pageLength: 25,
                responsive: true,
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },],
            });

        },

    },
    // Customers
    // ------------------------------------------------------------------------
    subcategories: {

        index: function () {
            $('#subcategory-table').DataTable({
                pageLength: 25,
                responsive: true,
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },],
            });

        },

    },
    // Deliverycharges
    // ------------------------------------------------------------------------
    deliverycharges: {

        index: function () {
            $('#deliverycharge-table').DataTable({
                pageLength: 25,
                responsive: true,
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },],
            });

        },

    },
    // Coupons
    // ------------------------------------------------------------------------
    coupons: {

        index: function () {
            $('#coupon-table').DataTable({
                pageLength: 25,
                responsive: true,
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },],
            });

        },
        details: function () {
            $('#id_category').bootstrapDualListbox({
                nonSelectedListLabel: 'Available Categories',
                selectedListLabel: 'Chosen Categories',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });
            $('#id_sub_category').bootstrapDualListbox({
                nonSelectedListLabel: 'Available Sub Categories',
                selectedListLabel: 'Chosen Sub Categories',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });
            $('#id_product').bootstrapDualListbox({
                nonSelectedListLabel: 'Available Product',
                selectedListLabel: 'Chosen Product',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });
            $('#id_discount_type').on('change', function(){
                var typeValue = $(this).val()
                if(typeValue == "Fixed"){
                    $('#div_id_discount_amount').parent().show()
                    $('#div_id_discount_percentage, #div_id_buy_product_count, #div_id_get_free_product_count').parent().hide()
                }else if(typeValue == "Percentage"){
                    $('#div_id_discount_amount, #div_id_buy_product_count, #div_id_get_free_product_count').parent().hide()
                    $('#div_id_discount_percentage').parent().show()
                }else if(typeValue.length == "Buy Qty Get Qty Free".length){
                    $('#div_id_discount_amount, #div_id_discount_percentage').parent().hide()
                    $('#div_id_buy_product_count, #div_id_get_free_product_count').parent().show()
                }else if(typeValue.length == "Buy More Than Amount Get Qty Free".length){
                    $('#div_id_discount_amount, #div_id_discount_percentage, #div_id_buy_product_count').parent().hide()
                    $('#div_id_get_free_product_count').parent().show()
                }else if(typeValue.length == "Buy More Than Amount Get Amount Free".length){
                    $('#div_id_discount_percentage, #div_id_buy_product_count, #div_id_get_free_product_count').parent().hide()
                    $('#div_id_discount_amount').parent().show()
                }else if(typeValue.length == "Buy More Than Amount Get Percentage Free".length){
                    $('#div_id_discount_amount, #div_id_buy_product_count, #div_id_get_free_product_count').parent().hide()
                    $('#div_id_discount_percentage').parent().show()
                }else{
                    $('#div_id_discount_amount, #div_id_discount_percentage, #div_id_buy_product_count, #div_id_get_free_product_count').parent().show()
                }
            });
        },

    },
    // expense
    // ------------------------------------------------------------------------
    expenses: {

        index: function () {
            $('#expense-table').DataTable({
                pageLength: 25,
                responsive: true,
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },],
            });

        },

    },
    // expensetypes
    // ------------------------------------------------------------------------
    expensetypes: {

        index: function () {
            $('#expensetype-table').DataTable({
                pageLength: 25,
                responsive: true,
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },],
            });

        },

    },
    // plans
    // ------------------------------------------------------------------------
    plans: {

        index: function () {
            $('#plan-table').DataTable({
                pageLength: 25,
                responsive: true,
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },],
            });

        },

    },
    // stores
    // ------------------------------------------------------------------------
    stores: {

        index: function () {
            $('#store-table').DataTable({
                pageLength: 25,
                responsive: true,
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },],
            });

        },
        details: function () {
            $('#id_delivery_boys').bootstrapDualListbox({
                nonSelectedListLabel: 'Available Delivery Boys',
                selectedListLabel: 'Chosen Delivery Boys',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });
        },

    },
    // products
    // ------------------------------------------------------------------------
    products: {
        index: function () {
            $('#product-table').DataTable({
                pageLength: 25,
                responsive: true,
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },],
            });

        },
        details: function () {

        },

    },
    // storeproducts
    // ------------------------------------------------------------------------
    storeproducts: {
        index: function () {
            $('#storeproduct-table').DataTable({
                pageLength: 25,
                responsive: true,
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },],
            });

        },
        details: function () {

        },

    },
    // storemanagers
    // ------------------------------------------------------------------------
    storemanagers: {
        index: function () {
            $('#storemanager-table').DataTable({
                pageLength: 25,
                responsive: true,
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },],
            });

        },

    },
    // orders
    // ------------------------------------------------------------------------
    orders: {
        index: function () {
            $('#order-table').DataTable({
                pageLength: 25,
                responsive: true,
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },],
            });

        },
        details: function () {
            $('#id_product').bootstrapDualListbox({
                nonSelectedListLabel: 'Available Product',
                selectedListLabel: 'Chosen Product',
                preserveSelectionOnMove: 'moved',
                moveOnSelect: false
            });
        },

    },
    // memberships
    // ------------------------------------------------------------------------
    memberships: {
        index: function () {
            $('#membership-table').DataTable({
                pageLength: 25,
                responsive: true,
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },],
            });

        },

    },
    // deliveryboys
    // ------------------------------------------------------------------------
    deliveryboys: {
        index: function () {
            $('#deliveryboy-table').DataTable({
                pageLength: 25,
                responsive: true,
                columnDefs: [{
                    orderable: false,
                    targets: -1
                },],
            });

        },
        details: function () {
            $('#id_birth_date').daterangepicker({
                singleDatePicker: true,
                locale: {
                    format: 'YYYY-MM-DD'
                }
            });
        },

    },
};
