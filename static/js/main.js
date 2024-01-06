$(() => {
    $('#signin').on('click', (e) => {
        e.preventDefault()
       $('#signup-card form input').remove()
       $('#signup-card h3').text('Sign in')
       $('<input type="email" value="" />')
       .attr('type', 'email')
       .attr('name', 'email')
       .attr('placeholder', 'E-mail')
       .appendTo('#signup-card form')

       $('<input type="password" value="" />')
       .attr('type', 'password')
       .attr('name', 'password')
       .attr('placeholder', 'Password')
       .appendTo('#signup-card form')

       $('<input type="submit" value="Sign in" id="signin">')
       .attr('method', 'post')
       .appendTo('#signup-card form')

    })

    $('#clipboardPasswd').on('click', (e) => {
            e.preventDefault()
            var password = document.getElementById('generated-password').innerHTML
            navigator.clipboard.writeText(password)     
    })
    

})