<template>
  <q-page>
    <div class="header">
      <div class="content q-py-sm">
        <h1 class="text-italic text-center text-h3 q-mt-lg q-mb-sm no-padding">Bienvenue</h1>
        <h2 class="text-center text-h5 q-mt-sm q-mb-lg">
          dans le <span class="text-uppercase">c</span>ercle d'<span class="text-uppercase">en</span>traide<br/>
          et d'<span class="text-uppercase">e</span>change de <span class="text-uppercase">mat</span>ériel
        </h2>
      </div>
    </div>

    <div class="q-px-md">
      <h2 class="text-h4 q-mb-md">
        Une association d'agriculteurs, pourquoi faire ?
      </h2>

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

      <h2 class="text-h4 q-my-md">
        Rejoindre le CENEMAT
      </h2>

      <div class="row">
        <div class="col-12 col-md-4 q-pa-sm">
          <q-btn
            stack
            class="full-width"
            color="primary"
            label="06 86 43 01 67"
            icon="phone"
            href="tel:0686430167"
          />
        </div>

        <div class="col-12 col-md-4 q-pa-sm">
          <q-btn
            stack
            class="full-width"
            color="primary"
            label="association.cenemat@wanadoo.fr"
            icon="mail"
            href="mailto:association.cenemat@wanadoo.fr"
          />
        </div>

        <div class="col-12 col-md-4 q-pa-sm">
          <q-btn
            stack
            class="full-width"
            color="primary"
            label="16 chemin de Rougemon 39100 FOUCHERANS"
            icon="map"
            target="_blank"
            href="https://www.google.com/maps/place/16+Chem.+de+Rougemont,+39100+Foucherans/"
          />
        </div>
      </div>

      <p class="q-mt-lg text-italic">
        Le CENEMAT est une association de loi 1901, il fonctionne grâce aux cotisations de ses adhérents.
      </p>
      <p>
        La cotisation est de <span class="text-weight-bold">130</span> euros.
      </p>
    </div>
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

  .content {
    width: 100%;
    height: 100%;
    background-color: rgba(255, 255, 255, 0.5);
  }
}
h1 {
  padding-top: 5rem;
}
</style>
