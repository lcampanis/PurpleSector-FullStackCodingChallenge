import { defineConfig, PluginOption, HmrContext } from "vite";
import react from "@vitejs/plugin-react";
import tsconfigPaths from "vite-tsconfig-paths";

const fullReloadAlways: PluginOption = {
  name: "full-reload-always",
  handleHotUpdate({ server }: HmrContext) {
    server.ws.send({ type: "full-reload" });
    return [];
  },
};
// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react(), tsconfigPaths(), fullReloadAlways],
});
