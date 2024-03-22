<template>
  <h3 class="px-15 pa-10">Bookmarks</h3>
  <div>
    <v-row align="start" justify="center" wrap class="ga-4 flex-wrap w-100 px-15">
      <v-col v-for="i in 5" :key="i">
        <v-card max-width="322" min-width="300">
          <v-card-item>
            <div>
              <div class="text-overline mb-1">
              </div>
              <div class="text-h6 mb-1">
                Headline
              </div>
              <div class="text-caption">Greyhound divisely hello coldly fonwderfully</div>
            </div>
          </v-card-item>

          <v-card-actions>
            <v-btn>
              Open
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>