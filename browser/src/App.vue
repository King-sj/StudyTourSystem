<script setup lang="ts">
import { RouterView } from 'vue-router'
import { useRouter } from 'vue-router';

const router = useRouter()
router.push({ name: "home" })

</script>

<template>
  <main>
    <n-layout embedded has-sider style="height:100%;width: 100vw;">
      <n-layout-sider collapse-mode="transform" :native-scrollbar="true" show-trigger="bar"
        content-style="padding: 0px;" :inverted="true" :show-collapsed-content="false" :default-collapsed="true"
        :collapsed-width="1"
        bordered>
        <n-flex vertical style="height:100%">
          <n-button quaternary size="large" type="info" style="font-size: 3.5rem;margin: 2rem;"
            @click="router.push({ name: 'home' })">
            Home
          </n-button>
          <n-divider />

          <n-button quaternary size="large" type="info" style="font-size: 3.5rem;margin: 2rem;"
            @click="router.push({ name: 'history' })">
            History
          </n-button>
          <n-divider />

          <n-button quaternary size="large" type="info" style="font-size: 3.5rem;margin: 2rem;"
            @click="router.push({ name: 'jours' })">
            All Jour
          </n-button>
          <n-divider />


          <n-button quaternary size="large" type="info" style="font-size: 3.5rem;margin: 2rem;"
          @click="router.push({name:'setting'})"
        >
          Settings
        </n-button>
        <n-divider />
        </n-flex>
      </n-layout-sider>

      <n-layout-content content-style="padding: 24px;">
          <router-view />
      </n-layout-content>
    </n-layout>
  </main>
</template>

<style lang="scss" scoped>
.n-button{
  margin: 0;
  padding: 0;
}
*{
  background-color: var(--color-background);
  color: var(--color-text);
}
</style>
