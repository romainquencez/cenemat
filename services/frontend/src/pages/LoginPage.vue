<template>
  <q-page class="q-pa-md">
    <div class="row">
      <div class="col-sm-2 col-lg-4"></div>

      <div class="col-xs-12 col-sm-8 col-lg-4">
        <h3>Connectez-vous</h3>

        <q-form
          @submit="onSubmit"
          class="q-gutter-md"
        >
          <q-input
            filled
            v-model="email"
            type="email"
            label="Email *"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'Requis']"
          />

          <q-input
            filled
            type="password"
            v-model="password"
            label="Mot de passe *"
            lazy-rules
            :rules="[ val => val && val.length > 0 || 'Requis']"
          />

          <q-btn
            label="Connexion"
            type="submit"
            color="positive"
            class="full-width"
          />
        </q-form>
      </div>
    </div>
  </q-page>
</template>

<script lang="ts">
import { useQuasar } from 'quasar'
import { defineComponent, ref } from 'vue'
import { useUserStore } from 'stores/users'
import { useRouter } from 'vue-router'

export default defineComponent({
  name: 'LoginPage',
  setup () {
    const $q = useQuasar()
    const email = ref(null)
    const password = ref(null)
    const userStore = useUserStore()
    const router = useRouter()
    const onSubmit = async () => {
      $q.loading.show()

      const User = new FormData()
      User.append('username', email.value)
      User.append('password', password.value)
      return await userStore.logIn(User).then(() => {
        $q.notify({
          color: 'green-4',
          textColor: 'white',
          icon: 'cloud_done',
          message: 'Connecté'
        })
        // redirect user to his page
        router.push({name: 'user'})
      }).catch(() => {
        // show error message
        $q.notify({
          color: 'red-4',
          textColor: 'white',
          icon: 'error',
          message: 'Mauvaise combinaison email / mot de passe.'
        })
      }).finally(() => {
        $q.loading.hide()
      })
    }

    return {
      email,
      password,
      onSubmit,
    }
  }
});
</script>
