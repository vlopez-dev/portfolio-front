<script>
  import { onMount } from "svelte";
  let projects=[]

  onMount(async () => {
  fetch("http://127.0.0.1:8000/project/")
  .then(response => response.json())
  .then(data => {
    projects=data
    console.log(projects)
		// console.log(data);
  }).catch(error => {
    console.log(error);
    return [];
  });
});

</script>



<section class="hero is-fullheight">
<div class="hero-body">
<div class="container is-fluid">

  <div class="columns  is-multiline">
    {#each projects as project}

    <div class="column is-one-quarter-desktop is-half-tablet">


          <div class="card">
          <img class="" src="{project.pro_img}" alt="Placeholder image">
          <div class="info">
            <h2 class="">{project.name}</h2>
            <p class="">{project.description}</p>
            <button>Info
				
			</button>
          </div>
        </div>
     </div>


    {/each}

  </div>

</div>
</div>
  </section>







<style>
	
.hero{
    background-color: #fced73;
       }
   

.card{
  	width: 682px;
	height: 400px;
	border-radius: 15px;
	padding: 1.5rem;
	background: white;
	position: relative;
	display: flex;
	align-items: flex-end;
	transition: 0.4s ease-out;
  	-webkit-box-shadow: 5px 5px 15px 5px #000000; 
  	box-shadow: 5px 5px 15px 5px #000000;

}



.card:hover{
	transform: translateY(20px);
}

.card:hover::before{
	opacity: 1;
}


.card:hover .info{
	opacity: 1;
	transform: translateY(0px);


}

.card::before{
	content: "";
	position: absolute;
	top: 0;
	left: 0;
	left: 0;
	display: block;
	width: 100%;
	height: 100%;
	border-radius: 15px;
	background: rgba(0, 0, 0, 0.6);
	z-index: 2;
	transition: 0.5s;
	opacity: 0;
}

.card img{
	width: 100%;
	height: 100%;
	-o-object-fit: cover;
	object-fit: cover;
	position: absolute;
	top: 0;
	left: 0;
	border-radius: 15px;
	align-items: center;

}

.card .info{
	position: relative;
	z-index: 3;
	color: white;
	opacity: 0;
	transform: translateY(30px);
	transition: 0.5s;

}

.card .info h1{
	margin: 0px;
}
.card .info p{
	letter-spacing: 1px;
	font-size: 15px;
	margin-top: 8px;
}

.card .info button{
	padding: 0.6rem;
	outline: none;
	border: none;
	border-radius: 3px;
	background: white;
	color: black;
	font-weight: bold;
	cursor: pointer;
	transition: 0.4s ease;
}

.card .info button:hover{
	background: dodgerblue;
	color: white;
}

</style>