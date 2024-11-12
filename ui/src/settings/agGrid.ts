import "@ag-grid-community/styles/ag-grid.css";
import "@ag-grid-community/styles/ag-theme-quartz.css";

import { ModuleRegistry } from "@ag-grid-community/core";
import { ClientSideRowModelModule } from "@ag-grid-community/client-side-row-model";
import { CsvExportModule } from "@ag-grid-community/csv-export";

/**
 * https://www.ag-grid.com/react-data-grid/modules/
 */
ModuleRegistry.registerModules([ClientSideRowModelModule, CsvExportModule]);
