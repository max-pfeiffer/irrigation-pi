import { CommonModule } from '@angular/common';
import {
  ChangeDetectionStrategy,
  ChangeDetectorRef,
  Component,
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
  standalone: true,
  changeDetection: ChangeDetectionStrategy.OnPush,
  imports: [
    CommonModule,
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
  public relays: Relay[] = [];

  constructor(
    public relayService: RelayService,
    public cdr: ChangeDetectorRef
  ) {}

  public ionViewDidEnter(): void {
    this.refreshList();
  }

  public refreshList(): void {
    this.relayService.getRelays().subscribe({
      next: (_relays: Relay[]) => {
        this.relays = _relays;
        this.cdr.detectChanges();
      },
    });
  }
}
