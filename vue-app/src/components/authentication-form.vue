<template>
  <div class="limiter">
    <div class="container-login100">
      <div class="wrap-login100 p-t-5 p-b-20">
					<span class="login100-form-title">
						ShareLoc
					</span>
        <div class="wrap-input100 validate-input m-t-50 m-b-35" data-validate="Enter username">
          <input class="input100" type="text" name="username" v-model="username">
          <span class="focus-input100" data-placeholder="Username"></span>
        </div>

        <div class="wrap-input100 validate-input m-b-50" data-validate="Enter password">
          <input class="input100" type="password" name="pass" v-model="password">
          <span class="focus-input100" data-placeholder="Password"></span>
        </div>

        <div class="container-login100-form-btn">
          <button v-on:click="login()" class="login100-form-btn">
            Login
          </button>
        </div>
      </div>
    </div>
  </div>
</template>


<script>

  export default {
    data: function () {
      return {
        username: "",
        password: ""
      }
    },
    methods: {
      login() {
        console.log(this.username, this.password)
      }
    }
  }
</script>

<style>
  @import "../assets/vendor/bootstrap/css/bootstrap.min.css";
  /*@import "../assets/fonts/font-awesome-4.7.0/css/font-awesome.min.css";*/
  /*@import "../assets/fonts/iconic/css/material-design-iconic-font.min.css";*/
  @import "../assets/vendor/animate/animate.css";
  @import "../assets/vendor/css-hamburgers/hamburgers.min.css";
  @import "../assets/vendor/animsition/css/animsition.min.css";
  @import "../assets/vendor/select2/select2.min.css";
  @import "../assets/vendor/daterangepicker/daterangepicker.css";
  @import "../assets/css/util.css";
  @import "../assets/css/main.css";
</style>
