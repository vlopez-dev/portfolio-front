<script>
    export let item1, item2, item3,item4
</script>

<header>
        <nav class="navbar  is-transparent" role="navigation" aria-label="main navigation">
            <div class="navbar-brand">
            <a class="navbar-item" href="https://bulma.io">
                <img src="https://bulma.io/images/bulma-logo.png" width="112" height="28">
            </a>
        
            <a role="button" class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbarBasicExample">
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
                <span aria-hidden="true"></span>
            </a>
            </div>
        
            <div id="navbarBasicExample" class="navbar-menu">
            <div class="navbar-start">
                <a class="navbar-item">
                {item1}
                </a>
        
                <a class="navbar-item">
                {item2}
                </a>
                <a class="navbar-item">
                    {item3}
                    </a>
                    <a class="navbar-item">
                        {item4}
                        </a>
          
            </div>
        </nav>



    </header>
<style>
    header{
        width: 100%;
    }
</style>