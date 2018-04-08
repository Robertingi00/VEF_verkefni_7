%include('template/header.tpl')
	<div class="wrapper-shop">
	<section>
		<div class="head"></div>
		
		<div class="box">
            % for x in products:
              <div class="row">
                <div class="product size">
                  <div class="title">
                    <h3>{{x['name']}}</h3>
                  </div>
                  <div class="img"><img src="/static/{{x['pid']}}.png" style="width: 268px; height:268px;"></div>
                  <ul class="option">
                    <li class="price"><a href="#">
                    % tmp = "{:,}".format(x['price'])
			    	{{tmp}}</a></li>
                    <li class="buy"><a class="box1" href="/cart/add/{{x['pid']}}">Add To Cart</a></li>
                  </ul>
                </div> 
              </div>
            % end
        </div>
	</section>



	<script>
	function w3_open() {
	    document.getElementById("mySidebar").style.display = "block";
	}
	function w3_close() {
	    document.getElementById("mySidebar").style.display = "none";
	}
	</script>
</body>
</html>