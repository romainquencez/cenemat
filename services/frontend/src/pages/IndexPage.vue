<template>
  <q-page class="header text-white">
    <h1 class="text-italic text-center no-margin">Bienvenue</h1>
    <h2 class="text-center">
      dans le <span class="text-uppercase">c</span>ercle d'<span class="text-uppercase">en</span>traide<br/>
      et d'<span class="text-uppercase">e</span>change de <span class="text-uppercase">mat</span>ériel
    </h2>

  </q-page>

  <q-page>
    <h3>
      Une association d'agriculteurs, pourquoi faire ?
    </h3>

    <p>
      <q-icon name="check" /> Réaliser ses travaux agricoles au bon moment dans de bonnes conditions.<br />
      <q-icon name="check" /> Faire face en cas de panne de matériel.<br />
      <q-icon name="check" /> Bénéficier de matériels spécialisés et performants sans avoir à investir.<br />
      <q-icon name="check" /> Rentabiliser son matériel en travaillant pour d'autres en tant qu'offreur.<br />
      <q-icon name="check" /> Diminuer ses charges de mécanisation.<br />
      <q-icon name="check" /> Différer ou éviter un investissement trop lourd.<br />
      <q-icon name="check" /> Organiser des chantiers efficaces et rapides.<br />
      <q-icon name="check" /> Diminuer les pointes de travail.<br />
      <q-icon name="check" /> Profiter de la disponibilité et de la compétence d'autres agriculteurs en travaillant ensemble.
    </p>

    <hr />

    <h3>
      Rejoindre le CENEMAT
    </h3>

    <p>
      <q-icon name="phone" /> <a href="phone:+33686430167">06 86 43 01 67</a><br />
      <q-icon name="email" /> <a href="mailto:association.cenemat@wanadoo.fr">association.cenemat@wanadoo.fr</a><br />
      <q-icon name="house" /> <a href="https://www.google.com/maps/place/16+Chem.+de+Rougemont,+39100+Foucherans/" target="_blank">16, chemin de Rougemon 39100 FOUCHERANS</a>
    </p>

    <p>
      <span class="text-italic">Le CENEMAT est une association de loi 1901, il fonctionne grâce aux cotisations de ses adhérents.</span><br />
      La cotisation est de <span class="text-weight-bold">130</span> euros.
    </p>
  </q-page>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'IndexPage',
});
</script>

<style lang="scss" scoped>
.header {
  background: url('assets/background.png') no-repeat;
  background-size: cover;
}
h1 {
  padding-top: 5rem;
}
</style>
