<template>
  <div style="max-width: 50vw; margin: auto; margin-top: 20vh">
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
</template>

<script lang="ts">
import { useQuasar } from 'quasar'
import { defineComponent, ref } from 'vue';

export default defineComponent({
  name: 'LoginPage',
  setup () {
    const $q = useQuasar()
    const email = ref(null)
    const password = ref(null)

    return {
      email,
      password,
      onSubmit () {
        $q.notify({
          color: 'green-4',
          textColor: 'white',
          icon: 'cloud_done',
          message: 'Connecté'
        })
      }
    }
  }
});
</script>
