import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'

import App from './App.vue'
import router from './router'

import 'leaflet/dist/leaflet.css';

// import BaiduMapOffline from 'vue-baidu-map-offline';
import BaiduMap from 'vue-baidu-map-3x';

const app = createApp(App)

app.use(createPinia())
app.use(router)

// app.use(BaiduMapOffline, {
//   offline: true
// });
app.use(BaiduMap, {
  // ak 是在百度地图开发者平台申请的密钥 详见 http://lbsyun.baidu.com/apiconsole/key */
  ak: 'inP2p61su5yuLvkPBk62POprLY3um0L4',
  // v:'2.0',  // 默认使用3.0
  // type: 'WebGL' // ||API 默认API  (使用此模式 BMap=BMapGL)
});

app.mount('#app')
