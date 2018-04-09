%include('template/header.tpl')
<div class="wrapper-signup">
	<section>
		<article>
			<img src="/static/logo.svg">
			<h1>Staff sign in</h1>
			<p></p>
			<form action="login" method="POST">
				<input type="text" name="username" placeholder="User" required>
				<input type="password" name="password" placeholder="Password" required>
				<input type="submit">
			</form>
		</article>
	</section>
</div>
