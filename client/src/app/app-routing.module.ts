import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import {HomeComponent} from "./home/home.component";
import {AddVehicleComponent} from "./add-vehicle/add-vehicle.component";
import {RemoveVehicleComponent} from "./remove-vehicle/remove-vehicle.component";

const routes: Routes = [
  {path: 'home', component: HomeComponent},
  {path: 'addVehicle', component: AddVehicleComponent},
  {path: 'removeVehicle', component: RemoveVehicleComponent},
  {path: '**', component: HomeComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
