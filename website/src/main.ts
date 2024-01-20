import { ɵprovideZonelessChangeDetection } from "@angular/core";
import { bootstrapApplication } from "@angular/platform-browser";
import { AppComponent } from "./app/app.component";

bootstrapApplication(AppComponent, {
  providers: [ɵprovideZonelessChangeDetection()],
}).catch((e) => console.error(e));
