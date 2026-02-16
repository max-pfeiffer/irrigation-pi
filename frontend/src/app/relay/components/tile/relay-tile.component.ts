import {
  ChangeDetectionStrategy,
  Component,
  inject,
  input,
  output,
} from '@angular/core';
import { FormsModule } from '@angular/forms';
import { IonItem, IonToggle } from '@ionic/angular/standalone';
import { finalize } from 'rxjs';
import { Relay } from '../../models/relay.models';
import { RelayService } from '../../services/relay.service';

@Component({
  selector: 'app-relay-tile',
  templateUrl: './relay-tile.component.html',
  styleUrls: ['./relay-tile.component.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  imports: [FormsModule, IonItem, IonToggle],
})
export class RelayTileComponent {
  public relayService = inject(RelayService);

  public relay = input<Relay>();
  public refreshList = output();

  public onRelayToggle(event: CustomEvent<{ checked: boolean }>) {
    let { position, ...payload } = this.relay();
    payload = { ...payload, on: event.detail.checked };
    this.relayService
      .updateRelay(this.relay().position, payload)
      .pipe(
        finalize(() => {
          this.refreshList.emit();
        }),
      )
      .subscribe();
  }
}
