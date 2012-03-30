<%inherit file="../base.mako"/>
<%def name="title()">
    Register account
</%def>
<h2>Register!</h2>
<form method="POST" action="/user/register">
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
