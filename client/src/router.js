import Vue from "vue";
import VueRouter from "vue-router";
import paymentcard from "./components/PaymentCard";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "home",
    component: paymentcard
  }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
