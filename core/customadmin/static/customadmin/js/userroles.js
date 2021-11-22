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
                    format: 'MM/DD/YYYY'
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
                //     { data: 'name', name: 'name' },
                //     // { data: 'actions', name: 'actions' },
                // ],
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
            $('#id_start_date').daterangepicker({
                timePicker: true,
                timePickerIncrement: 15,
                singleDatePicker: true,
                startDate: moment().startOf('hour'),
                endDate: moment().add(1, 'hour'),
                minDate: moment(),
                autoUpdateInput: true,
                locale: {
                    format: 'MM/DD/YYYY hh:mm A'
                }
            });
            $('#id_expiry_date').daterangepicker({
                timePicker: true,
                timePickerIncrement: 15,
                singleDatePicker: true,
                startDate: moment().startOf('hour'),
                endDate: moment().add(1, 'hour'),
                minDate: moment(),
                autoUpdateInput: true,
                locale: {
                    format: 'MM/DD/YYYY hh:mm A'
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
};
