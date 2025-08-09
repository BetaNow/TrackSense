<template>
  <div class="p-6 max-w-4xl mx-auto">
    <h1 class="text-2xl font-bold mb-4">PitStop-AI Lite — Timeline Viewer</h1>
    <input type="file" accept=".json" @change="onFile" class="mb-4"/>
    <div v-if="timeline">
      <p class="mb-2"><b>Video:</b> {{ timeline.video_id }} — <b>FPS:</b> {{ timeline.fps }}</p>
      <ul class="list-disc pl-6">
        <li v-for="(e,i) in timeline.events" :key="i">
          [{{ e.type }}] {{ e.label || '—' }} at {{ e.t ?? e.t_start }}s (conf={{ e.confidence ?? '—' }})
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
const timeline = ref<any|null>(null)
const onFile = async (evt: Event) => {
  const file = (evt.target as HTMLInputElement).files?.[0]
  if (!file) return
  const text = await file.text()
  timeline.value = JSON.parse(text)
}
</script>
