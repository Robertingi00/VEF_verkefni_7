%include('template/header.tpl')
<div class="wrapper-sida2">
	<h3>Karfa:</h3>

  % if len(karfa) > 0:
	  <table class="customers">
		  <tr>
		    <th>Item img</th>
		    <th>Item name</th>
		    <th>Option</th>
		    <th></th>
		  </tr>
		  % for x in karfa:
			  <tr>
			    <td><img src="/static/{{x['pid']}}.png" style="width: 5em;"></td>
			    <td>{{x['name']}}</td>
			    <td>
			    	% tmp = "{:,},-".format(x['price'])
			    	{{tmp}}<h5 style="display: inline">/kr,-</h5></td>
			    <td style="text-align: right;"><a href="/cart/del/{{x['pid']}}"><img src="/static/trash.png" style="width: 4em;"></a></td>
			  </tr>
		  % end
		  <tr>
		  	<td></td>
		  	<td>Samanlagt:</td>
		  	<td>
		  		% tmp = "{:,},-".format(summa)
		  		{{tmp}}
		  		<h5 style="display: inline">/kr,-</h5>
		  	<td></td>
		  	</td>
		  </tr>
	  </table>
	  <div class="">
		   <a class="" href="/cart/remove">❮ Eyða körfu</a>
		   <a class="" href="#fdfdfd" style="float: right;">Klára körfu ❯</a>
	  </div>
  % else:
  <h3>Karfan Þín er tóm þú verður að velja þér vörur</h3>
  <h3><a href="/shop">Ýttu hérna ef þú villt fara til baka og velja vörur</a></h3>
	
</div>