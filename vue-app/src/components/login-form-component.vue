<template xmlns:v-on="http://www.w3.org/1999/xhtml">
  <div class="limiter">
    <div class="container-login100">
      <div class="wrap-login100 p-t-10 p-b-10">
					<span class="login100-form-title p-b-20">
						ShareLoc
					</span>
        <div class="wrap-input100 validate-input m-t-10 m-b-35" data-validate="Enter username">
          <input v-model='username' class="input100" type="text" name="username">
        </div>

        <div class="wrap-input100 validate-input m-b-35" data-validate="Enter password">
          <label v-if="password_incorrect" for="password">Password incorrect</label>
          <input id="password" v-model='password' class="input100" type="password" name="pass">
        </div>

        <div class="container-login100-form-btn">
          <button v-on:click="login" class="login100-form-btn">
            Login
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        password_incorrect: false,
        username: '',
        password: ''
      }
    },
    methods: {
      login: function () {
        var self = this;
        this.$http.post('http://0.0.0.0:8000/rest-auth/login', {
          'username': this.username,
          'password': this.password
        }).then(response => {
            console.log(response.body.token);
          localStorage.setItem('token', response.body.token);
          self.$router.push('/map');
        }, response => {
          console.log("Error");
          this.password_incorrect = true;
        });
      }
    }
  }
</script>


<style>
</style>
