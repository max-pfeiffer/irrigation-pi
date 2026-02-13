import {
  ChangeDetectionStrategy,
  Component,
  inject,
  signal,
} from '@angular/core';
import {
  IonButtons,
  IonContent,
  IonHeader,
  IonList,
  IonMenuButton,
  IonTitle,
  IonToolbar,
  ViewDidEnter,
} from '@ionic/angular/standalone';
import { RelayTileComponent } from '../../components/tile/relay-tile.component';
import { Relay } from '../../models/relay.models';
import { RelayService } from '../../services/relay.service';

@Component({
  selector: 'app-relay-list',
  templateUrl: './relay-list.page.html',
  styleUrls: ['./relay-list.page.scss'],
  changeDetection: ChangeDetectionStrategy.OnPush,
  imports: [
    IonHeader,
    IonToolbar,
    IonButtons,
    IonMenuButton,
    IonTitle,
    IonContent,
    IonList,
    RelayTileComponent,
  ],
})
export class RelayListPage implements ViewDidEnter {
  public relayService = inject(RelayService);

  public relays = signal<Relay[]>([]);

  public ionViewDidEnter(): void {
    this.refreshList();
  }

  public refreshList(): void {
    this.relayService.getRelays().subscribe({
      next: (_relays: Relay[]) => {
        this.relays.set(_relays);
      },
    });
  }
}
