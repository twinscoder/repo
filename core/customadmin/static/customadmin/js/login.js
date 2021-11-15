/*global $ */
'use strict';

var login = {

    init: function (sso_url) {

        // Determine domains that should trigger SSO redirect
        $.get('/api/v1/core/sso-domains/', function (data) {

            let domains = data.data.domains;

            $('#id_username').on("change", function () {
                // Loop through all domains and see if any are in the username
                let email = $(this).val();

                for (let i in domains) {
                    let domain = domains[i];
                    var n = email.includes(domain);
                    if (n) {
                        $('form').remove();
                        $("p:first").addClass("lead").text("Redirecting you to the NBCU SSO page ...");
                        window.location.replace(sso_url);
                        break;
                    }
                }

            });

        }, 'json');

    }

};
