<%inherit file="../base.mako"/>
<%def name="title()">
    User view
</%def>
<h2>Login</h2>

<form method="POST" action="">
% for field in form:
<div>${ field.label} : ${ field } </div>

    % if field.errors:
        <ul class="errors">
            % for error in field.errors:
                <li>${error}</li>
            % endfor
        </ul>
    % endif

% endfor
</form>
