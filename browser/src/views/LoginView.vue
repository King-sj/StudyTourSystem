<script lang="ts" setup>
import { defineComponent, ref } from 'vue';
import axios from 'axios';
import { useRouter } from 'vue-router';
import { useStorage,useTimestamp } from '@vueuse/core'
import { useUserStore } from '@/stores/user';

const username = ref('');
const password = ref('');
const router = useRouter();
const userStore = useUserStore()
const login = async () => {
  try {
    // const { data } = await axios.post('http://localhost:5000/login', {
    //   username: username.value,
    //   password: password.value,
    // });

    // check
    userStore.update({
      name:username.value,
      lastLoginTimeStamp:useTimestamp().value
    })

    router.push({name:"home"})
  } catch (error) {
    console.error(error);
    alert('Login failed!');
  }
};
</script>

<template>
  <div>
    <h1>Login</h1>
    <form @submit.prevent="login">
      <div>
        <label for="username">Username:</label>
        <input v-model="username" type="text" id="username" required>
      </div>
      <div>
        <label for="password">Password:</label>
        <input v-model="password" type="password" id="password" required>
      </div>
      <button type="submit">Login</button>
    </form>
  </div>
</template>