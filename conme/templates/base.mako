<!DOCTYPE html>
<html lang="en">
<head>
	<meta charset="utf-8">
	<title>Convention Me!</title>
	<meta name="viewport" content="width=device-width, initial-scale=1.0">
	<meta name="description" content="">
	<meta name="author" content="">

	<!-- Styles -->
	<link href="../static/css/bootstrap.css" rel="stylesheet">
	<style>
		body {
			padding-top: 60px; /* 60px to make the container go all the way to the bottom of the topbar */
		}
	</style>
	<link href="../static/css/bootstrap-responsive.css" rel="stylesheet">

	<!-- HTML5 shim, for IE6-8 support of HTML5 elements -->
	<!--[if lt IE 9]>
		<script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
	<![endif]-->

</head>

<body>
	<div class="navbar navbar-fixed-top">
		<div class="navbar-inner">
			<div class="container">
				<a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
					<span class="icon-bar"></span>
				</a>
				<a class="brand" href="#">Convention Me!</a>
				<div class="nav-collapse">
					<ul class="nav">
						<a href="/">Home</a>
						<li><a href="#about">About</a></li>
						<li><a href="/user/login">Login</a></li>
						<li><a href="/user/logout">Logout</a></li>
						<li><a href="/user/register">Register</a></li>
					</ul>
				</div> <!--/.nav-collapse -->
			</div>
		</div>
	</div>

	<div class="container">
		${self.body()}
	</div> <!-- /container -->

	<!-- Le javascript
	================================================== -->
	<!-- Placed at the end of the document so the pages load faster -->
	<script src="../static/js/jquery.js"></script>
	<script src="../static/js/bootstrap-transition.js"></script>
	<script src="../static/js/bootstrap-alert.js"></script>
	<script src="../static/js/bootstrap-modal.js"></script>
	<script src="../static/js/bootstrap-dropdown.js"></script>
	<script src="../static/js/bootstrap-scrollspy.js"></script>
	<script src="../static/js/bootstrap-tab.js"></script>
	<script src="../static/js/bootstrap-tooltip.js"></script>
	<script src="../static/js/bootstrap-popover.js"></script>
	<script src="../static/js/bootstrap-button.js"></script>
	<script src="../static/js/bootstrap-collapse.js"></script>
	<script src="../static/js/bootstrap-carousel.js"></script>
	<script src="../static/js/bootstrap-typeahead.js"></script>
</body>
</html>