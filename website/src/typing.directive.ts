import {
  Directive,
  ElementRef,
  inject,
  input,
  OnDestroy,
  OnInit,
} from "@angular/core";
import { concatMap, delay, from, of, Subscription, tap } from "rxjs";

function type(val: string) {
  return [...Array(val.length + 1).keys()].map((i) => val.substring(0, i));
}

@Directive({
  selector: "[typing]",
  standalone: true,
})
export class TypingDirective implements OnInit, OnDestroy {
  private readonly el = inject(ElementRef);

  readonly delay = input(1000);
  readonly interval = input(100);

  private sub?: Subscription;

  ngOnDestroy() {
    this.sub?.unsubscribe();
  }
}
