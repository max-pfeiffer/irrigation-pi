import { CommonModule } from '@angular/common';
import {
  ChangeDetectionStrategy,
  Component,
  EventEmitter,
  Input,
  Output,
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
  standalone: true,
  changeDetection: ChangeDetectionStrategy.OnPush,
  imports: [CommonModule, FormsModule, IonItem, IonToggle],
})
export class RelayTileComponent {
  @Input()
  public relay: Relay;

  @Output()
  public refreshList = new EventEmitter<void>();

  public constructor(public relayService: RelayService) {}

  public onRelayToggle(event: CustomEvent<{ checked: boolean }>) {
    let { position, ...payload } = this.relay;
    payload = { ...payload, on: event.detail.checked };
    this.relayService
      .updateRelay(this.relay.position, payload)
      .pipe(
        finalize(() => {
          this.refreshList.emit();
        })
      )
      .subscribe();
  }
}
