import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'displayString',
  standalone: true,
})
export class DisplayStringPipe implements PipeTransform {
  capFirst(text: string): string {
    return text.charAt(0).toUpperCase() + text.slice(1);
  }

  transform(text: string): string {
    return this.capFirst(text.replace(/_/g, ' '));
  }
}
