<%inherit file="../base.mako"/>
<%def name="title()">
    User view
</%def>
<h2>Welcome to ConMe</h2>
<p>${user.id} - ${user.name} - ${user.email}</p>
